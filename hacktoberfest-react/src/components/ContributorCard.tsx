import { motion } from 'framer-motion';

interface ContributorProps {
  name: string;
  username: string;
  avatar: string;
  profile: string;
  contributions: number;
  location?: string;
  company?: string;
}

export default function ContributorCard({
  name,
  username,
  avatar,
  profile,
  contributions,
  location,
  company,
}: ContributorProps) {
  return (
    <motion.div
      className="bg-white/5 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg hover:shadow-xl transition-all duration-300 hover:bg-white/10"
      whileHover={{ y: -5 }}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div className="p-6">
        <div className="flex items-center space-x-4">
          <a href={profile} target="_blank" rel="noopener noreferrer" className="flex-shrink-0">
            <img
              className="w-16 h-16 rounded-full border-2 border-hacktoberfest-pink/30 hover:border-hacktoberfest-pink transition-all duration-300"
              src={avatar}
              alt={`${name}'s avatar`}
              loading="lazy"
            />
          </a>
          <div className="flex-1 min-w-0">
            <h3 className="text-lg font-semibold text-white truncate">
              <a href={profile} target="_blank" rel="noopener noreferrer" className="hover:text-hacktoberfest-pink transition-colors">
                {name || username}
              </a>
            </h3>
            <p className="text-sm text-gray-400 truncate">
              @{username}
            </p>
            {company && (
              <p className="text-sm text-gray-400 flex items-center mt-1">
                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fillRule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clipRule="evenodd" />
                  <path d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15a24.98 24.98 0 01-8-1.308z" />
                </svg>
                {company}
              </p>
            )}
            {location && (
              <p className="text-sm text-gray-400 flex items-center mt-1">
                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
                </svg>
                {location}
              </p>
            )}
          </div>
        </div>
        
        <div className="mt-4 flex items-center justify-between">
          <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-hacktoberfest-pink/10 text-hacktoberfest-pink">
            {contributions} {contributions === 1 ? 'contribution' : 'contributions'}
          </span>
          <a
            href={profile}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-medium text-hacktoberfest-pink hover:underline flex items-center"
          >
            View Profile
            <svg className="w-4 h-4 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          </a>
        </div>
      </div>
    </motion.div>
  );
}
