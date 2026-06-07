const DEPENDABOT_LOGINS = new Set([
  'app/dependabot',
  'dependabot[bot]',
  'dependabot-preview[bot]',
]);

const REBASE_MARKER = '<!-- dependabot-auto-rebase -->';
const REBASE_COOLDOWN_MS = 2 * 60 * 60 * 1000;

function isDependabot(user) {
  return user && DEPENDABOT_LOGINS.has(user.login);
}

function needsRebase(pull) {
  if (pull.state !== 'open' || pull.draft) {
    return false;
  }

  if (pull.mergeable === false) {
    return true;
  }

  return pull.mergeable_state === 'behind' || pull.mergeable_state === 'dirty';
}

function recentRebaseComment(comments) {
  const cutoff = Date.now() - REBASE_COOLDOWN_MS;
  return comments.some((comment) => {
    if (!comment.body || !comment.body.includes(REBASE_MARKER)) {
      return false;
    }
    if (comment.user?.login === 'github-actions[bot]') {
      return false;
    }
    return new Date(comment.created_at).getTime() >= cutoff;
  });
}

async function listOpenDependabotPulls(github, owner, repo) {
  const pulls = [];
  for (let page = 1; page <= 5; page += 1) {
    const { data } = await github.rest.pulls.list({
      owner,
      repo,
      state: 'open',
      per_page: 100,
      page,
    });
    if (data.length === 0) {
      break;
    }
    pulls.push(...data.filter((pull) => isDependabot(pull.user)));
    if (data.length < 100) {
      break;
    }
  }
  return pulls;
}

module.exports = async ({ github, context, core }) => {
  const { owner, repo } = context.repo;
  const pulls = await listOpenDependabotPulls(github, owner, repo);

  if (pulls.length === 0) {
    core.info('No open Dependabot pull requests.');
    return;
  }

  for (const pull of pulls) {
    const pullNumber = pull.number;
    const { data: fresh } = await github.rest.pulls.get({
      owner,
      repo,
      pull_number: pullNumber,
    });

    if (!needsRebase(fresh)) {
      core.info(
        `PR #${pullNumber} mergeable=${fresh.mergeable}, state=${fresh.mergeable_state} — rebase not needed`
      );
      continue;
    }

    const { data: comments } = await github.rest.issues.listComments({
      owner,
      repo,
      issue_number: pullNumber,
      per_page: 100,
    });

    if (recentRebaseComment(comments)) {
      core.info(`PR #${pullNumber} already has a recent auto-rebase comment — skip`);
      continue;
    }

    const body = [REBASE_MARKER, '@dependabot rebase'].join('\n');
    await github.rest.issues.createComment({
      owner,
      repo,
      issue_number: pullNumber,
      body,
    });
    core.info(`Requested Dependabot rebase on PR #${pullNumber}`);
  }
};
