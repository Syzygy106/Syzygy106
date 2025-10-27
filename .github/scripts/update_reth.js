const { graphql } = require('@octokit/graphql');
const fs = require('fs');


const token = process.env.GH_TOKEN;
const user = process.env.GH_USERNAME;
const owner = process.env.REPO_OWNER;
const repo = process.env.REPO_NAME;
const max = parseInt(process.env.MAX_ITEMS || '8', 10);


if (!token) throw new Error('Missing GH_TOKEN');


const client = graphql.defaults({
  headers: { authorization: `token ${token}` }
});


const q = `
  query($owner:String!, $name:String!, $user:String!, $n:Int!) {
    repository(owner:$owner, name:$name) {
      pullRequests(first:$n, states:[OPEN, MERGED], orderBy:{field:UPDATED_AT, direction:DESC},
                   filterBy:{headRefAuthor:$user}) {
        nodes { number, title, url, state, updatedAt }
      }
      issues(first:$n, states:OPEN, orderBy:{field:UPDATED_AT, direction:DESC},
             filterBy:{createdBy:$user}) {
        nodes { number, title, url, updatedAt }
      }
    }
  }
`;


(async () => {
  const data = await client(q, { owner, name: repo, user, n: max });
  const prs = data.repository.pullRequests.nodes
    .map(pr => `- PR [#${pr.number}](${pr.url}): ${pr.title} <sub>· ${pr.state} · ${pr.updatedAt.slice(0,10)}</sub>`);
  const issues = data.repository.issues.nodes
    .map(is => `- Issue [#${is.number}](${is.url}): ${is.title} <sub>· ${is.updatedAt.slice(0,10)}</sub>`);


  const lines = [
    prs.length ? '### Pull Requests' : '',
    ...prs,
    issues.length ? '\n### Issues' : '',
    ...issues
  ].filter(Boolean).join('\n');


  const content = lines || '- _No recent activity found._';
  const readme = fs.readFileSync('README.md', 'utf8');
  const updated = readme.replace(/(<!-- RETH:START -->)([\s\S]*?)(<!-- RETH:END -->)/,
    `$1\n${content}\n$3`);
  fs.writeFileSync('README.md', updated);
})();


