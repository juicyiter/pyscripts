/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/mengoreo/pyscripts/master/homebrew/brew_install)"

cd "$(brew --repo)"

git remote set-url origin git://mirrors.ustc.edu.cn/brew.git

cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"

git remote set-url origin git://mirrors.ustc.edu.cn/homebrew-core.git

brew update

echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile