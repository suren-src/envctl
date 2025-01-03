# To reload:
# source ~/.config/fish/config.fish .

# vim mode
fish_vi_key_bindings

set -U fish_greeting "Welcome to fish!"

# alias
abbr -a ll 'ls -lah'

# abbreviations
abbr -a k kubectl
abbr -a dc docker-compose

# Save this in ~/.config/fish/functions/setup_brew.fish
function setup_brew
    # Initialize brew environment
    eval (/opt/homebrew/bin/brew shellenv)

    # Setup completions only if directory doesn't exist
    if not test -d ~/.config/fish/completions
        mkdir -p ~/.config/fish/completions
        brew completions link
    end

    # Set Homebrew paths
    set -gx HOMEBREW_PREFIX "/opt/homebrew"
    set -gx HOMEBREW_CELLAR "/opt/homebrew/Cellar"
    set -gx HOMEBREW_REPOSITORY "/opt/homebrew"

    # Set Homebrew preferences
    set -gx HOMEBREW_NO_ENV_HINTS 1
    set -gx HOMEBREW_NO_ANALYTICS 1

    # Setup OpenSSL compile flags
    set -gx LDFLAGS "-L/opt/homebrew/opt/openssl@3/lib"
    set -gx CPPFLAGS "-I/opt/homebrew/opt/openssl@3/include"

    # Add Homebrew paths
    fish_add_path /opt/homebrew/bin
    fish_add_path /opt/homebrew/sbin
end

setup_brew