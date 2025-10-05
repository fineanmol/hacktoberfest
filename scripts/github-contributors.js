/**
 * Fetch contributors from GitHub API
 * This eliminates the need for manual contributorsList.js maintenance
 */

// Configuration
const REPO_OWNER = 'fineanmol';
const REPO_NAME = 'Hacktoberfest2025';
const GITHUB_API = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contributors`;

// Cache for contributors data
let contributorsCache = null;
let cacheTimestamp = null;
const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

/**
 * Fetch contributors from GitHub API with caching
 */
async function fetchGitHubContributors() {
  // Return cached data if still valid
  if (contributorsCache && cacheTimestamp && (Date.now() - cacheTimestamp < CACHE_DURATION)) {
    return contributorsCache;
  }

  try {
    const response = await fetch(GITHUB_API + '?per_page=100');
    
    if (!response.ok) {
      throw new Error(`GitHub API error: ${response.status}`);
    }

    const contributors = await response.json();
    
    // Transform to match your existing format
    contributorsCache = contributors.map((contributor, index) => ({
      id: index + 1,
      fullname: contributor.login,
      username: contributor.html_url,
      contributions: contributor.contributions,
      avatar_url: contributor.avatar_url
    }));

    cacheTimestamp = Date.now();
    return contributorsCache;
  } catch (error) {
    console.error('Error fetching contributors:', error);
    // Fallback to manual list if API fails
    return typeof contributors !== 'undefined' ? contributors : [];
  }
}

/**
 * Load contributors and render them
 */
async function loadContributors() {
  const loadingIndicator = document.getElementById('loading-contributors');
  const contributorsContainer = document.querySelector('.contributors');
  
  if (loadingIndicator) {
    loadingIndicator.style.display = 'block';
  }

  try {
    // Fetch from GitHub API
    const githubContributors = await fetchGitHubContributors();
    
    // Merge with manual list if it exists
    let allContributors = githubContributors;
    
    if (typeof contributors !== 'undefined' && contributors.length > 0) {
      // Keep manual entries that aren't on GitHub
      const githubUsernames = new Set(
        githubContributors.map(c => c.username.toLowerCase())
      );
      
      const manualOnly = contributors.filter(c => {
        const username = c.username.toLowerCase();
        return !githubUsernames.has(username);
      });
      
      allContributors = [...githubContributors, ...manualOnly];
    }

    // Re-index
    allContributors = allContributors.map((c, index) => ({
      ...c,
      id: index + 1
    }));

    // Update global Contributors variable
    window.Contributors = allContributors;
    
    // Update stats display
    const totalCountEl = document.getElementById('total-contributors-count');
    const githubCountEl = document.getElementById('github-contributors-count');
    
    if (totalCountEl) {
      totalCountEl.textContent = allContributors.length;
    }
    if (githubCountEl) {
      githubCountEl.textContent = githubContributors.length;
    }
    
    // Trigger your existing render function
    if (typeof render === 'function') {
      render();
    }

    if (loadingIndicator) {
      loadingIndicator.style.display = 'none';
    }

    console.log(`✅ Loaded ${allContributors.length} contributors (${githubContributors.length} from GitHub API)`);
    
  } catch (error) {
    console.error('Failed to load contributors:', error);
    
    // Fallback to manual list
    if (typeof contributors !== 'undefined') {
      window.Contributors = contributors;
      
      // Update stats for fallback
      const totalCountEl = document.getElementById('total-contributors-count');
      const githubCountEl = document.getElementById('github-contributors-count');
      
      if (totalCountEl) {
        totalCountEl.textContent = contributors.length;
      }
      if (githubCountEl) {
        githubCountEl.textContent = '0 (using fallback)';
        githubCountEl.style.fontSize = '1.2em';
      }
      
      if (typeof render === 'function') {
        render();
      }
      
      console.warn('⚠️ Using fallback contributors list (GitHub API failed)');
    }
    
    if (loadingIndicator) {
      loadingIndicator.style.display = 'none';
    }
  }
}

// Auto-load when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadContributors);
} else {
  loadContributors();
}

