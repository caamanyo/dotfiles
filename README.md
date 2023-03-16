# Dotfiles repo

Link to tutorial: https://www.atlassian.com/git/tutorials/dotfiles

## Clone dotfiles
1. Set alias in .zsh:

`alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'`

2. Ignore .cfg folder:

`echo ".cfg/" >> .gitignore`

3. Run:

```bash
git clone --bare https://github.com/caamanyo/dotfiles.git $HOME/.cfg
function config {
   /usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME $@
}
mkdir -p .config-backup
# Select desktop flavour
config branch desired-branch
config checkout
if [ $? = 0 ]; then
  echo "Checked out config.";
  else
    echo "Backing up pre-existing dot files.";
    config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
fi;
config checkout
config config status.showUntrackedFiles no
```
