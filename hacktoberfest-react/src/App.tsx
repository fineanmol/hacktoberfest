import { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ContributorCard from './components/ContributorCard';
import { FaSearch, FaGithub, FaStar } from 'react-icons/fa';
import { motion } from 'framer-motion';
// Import contributor lists from the monorepo root contributors folder
// These are JS arrays exported as default
// Path: ../../contributors/<file>.js
import listA from '../../contributors/contributorslist.js';
import listB from '../../contributors/contributorsList1.js';

interface Contributor {
  name: string;
  username: string;
  avatar: string;
  profile: string;
  contributions: number;
  location?: string;
  company?: string;
}

type RawContributor = { id: number; fullname: string; username: string };

function getLoginFromUrl(url: string): string {
  try {
    const u = new URL(url);
    const parts = u.pathname.split('/').filter(Boolean);
    return parts[0] || url; // fallback
  } catch {
    // not a valid URL, maybe it's already a login
    return url;
  }
}

type GithubUser = {
  login: string;
  avatar_url: string;
  html_url: string;
  name: string | null;
  company: string | null;
  location: string | null;
  public_repos: number;
};

export default function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [contributors, setContributors] = useState<Contributor[]>([]);
  const [loading, setLoading] = useState(true);
  const [visibleContributors, setVisibleContributors] = useState(12);
  const [profileCache, setProfileCache] = useState<Record<string, GithubUser>>({});

  useEffect(() => {
    const raws: RawContributor[] = ([] as RawContributor[])
      .concat((listA as RawContributor[]), (listB as RawContributor[]));
    // De-duplicate by login
    const seen = new Set<string>();
    const base: Contributor[] = [];
    for (const r of raws) {
      const profileUrl = r.username;
      const login = getLoginFromUrl(profileUrl);
      if (seen.has(login)) continue;
      seen.add(login);
      base.push({
        name: r.fullname || login,
        username: login,
        avatar: '',
        profile: profileUrl.startsWith('http') ? profileUrl : `https://github.com/${login}`,
        contributions: 0,
      });
    }
    setContributors(base);
    setLoading(false);
  }, []);

  const filteredContributors = contributors.filter(contributor => 
    contributor.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    contributor.username.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const loadMore = () => {
    setVisibleContributors(prev => prev + 12);
  };

  // Fetch GitHub profiles for currently visible entries and cache them
  useEffect(() => {
    if (loading) return;
    const slice = filteredContributors.slice(0, visibleContributors);
    const toFetch = slice
      .map(c => c.username)
      .filter(login => !(login in profileCache));
    if (toFetch.length === 0) return;
    // Limit batch size to avoid rate limit pressure
    const batch = toFetch.slice(0, 20);
    Promise.all(
      batch.map(async login => {
        try {
          const res = await fetch(`https://api.github.com/users/${login}`);
          if (!res.ok) throw new Error(`GitHub ${res.status}`);
          const data = (await res.json()) as GithubUser;
          return { login, data } as const;
        } catch (e) {
          return { login, data: undefined } as const;
        }
      })
    ).then(results => {
      setProfileCache(prev => {
        const next = { ...prev };
        for (const r of results) {
          if (r.data) next[r.login] = r.data;
        }
        return next;
      });
    });
  }, [filteredContributors, visibleContributors, loading]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-hacktoberfest-pink"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-900">
      <Navbar />
      
      <main className="flex-grow pt-24 px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <section className="text-center py-20">
          <motion.h1 
            className="text-5xl md:text-6xl font-bold mb-6 text-gradient"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            Hacktoberfest 2024
          </motion.h1>
          <motion.p 
            className="text-xl text-gray-300 max-w-3xl mx-auto mb-8"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.1 }}
          >
            A month-long celebration of open source! Contribute to open source and earn a limited edition T-shirt.
          </motion.p>
          <motion.div 
            className="flex flex-col sm:flex-row justify-center gap-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <a
              href="https://github.com/fineanmol/Hacktoberfest2024"
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary flex items-center justify-center gap-2"
            >
              <FaGithub className="w-5 h-5" />
              Star on GitHub
            </a>
            <a
              href="https://hacktoberfest.digitalocean.com/"
              target="_blank"
              rel="noopener noreferrer"
              className="border-2 border-hacktoberfest-pink text-hacktoberfest-pink hover:bg-hacktoberfest-pink/10 font-semibold py-3 px-6 rounded-lg transition-all duration-300 text-center"
            >
              Learn More
            </a>
          </motion.div>
        </section>

        {/* Contributors Section */}
        <section id="contributors" className="py-12">
          <div className="max-w-7xl mx-auto">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-white mb-4">Our Amazing Contributors</h2>
              <div className="divider"></div>
              <p className="text-gray-400 max-w-2xl mx-auto mb-8">
                Join these amazing contributors who have helped make this project better. Your contribution could be next!
              </p>
              
              <div className="relative max-w-md mx-auto mb-12">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <FaSearch className="text-gray-500" />
                </div>
                <input
                  type="text"
                  className="input-field pl-10"
                  placeholder="Search contributors..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>

              <div className="flex items-center justify-center gap-2 text-yellow-400 mb-8">
                <FaStar className="w-5 h-5" />
                <span>Star the repository to get the "Hacktoberfest-Accepted" label</span>
              </div>
            </div>

            {filteredContributors.length === 0 ? (
              <div className="text-center py-12">
                <p className="text-gray-400 text-lg">No contributors found matching "{searchTerm}"</p>
              </div>
            ) : (
              <>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                  {filteredContributors.slice(0, visibleContributors).map((contributor, index) => {
                    const cached = profileCache[contributor.username];
                    const name = (cached?.name || contributor.name || contributor.username);
                    const avatar = cached?.avatar_url || contributor.avatar;
                    const profile = cached?.html_url || contributor.profile;
                    const company = cached?.company || undefined;
                    const location = cached?.location || undefined;
                    const contributions = (cached?.public_repos ?? contributor.contributions);
                    return (
                      <motion.div
                        key={index}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.3, delay: index * 0.05 }}
                      >
                        <ContributorCard 
                          name={name as string}
                          username={contributor.username}
                          avatar={avatar}
                          profile={profile}
                          contributions={contributions}
                          company={company || undefined}
                          location={location || undefined}
                        />
                      </motion.div>
                    );
                  })}
                </div>

                {visibleContributors < filteredContributors.length && (
                  <div className="text-center mt-12">
                    <button
                      onClick={loadMore}
                      className="btn-primary"
                    >
                      Load More
                    </button>
                  </div>
                )}
              </>
            )}
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}
