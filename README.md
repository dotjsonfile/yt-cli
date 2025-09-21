# yt-cli

This is a simple CLI tool to search and play YouTube videos directly in your terminal.

## Prerequisites

- Python 3.6+ (recommended)
- `yt-dlp` for YouTube search and video extraction
- `mpv` (or another terminal-based video player like mplayer or vlc)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dotjsonfile/yt-cli.git
    cd yt-cli
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install a terminal-based media player (`mpv`, `mplayer`, or `vlc`):

    On **Ubuntu** or **Debian-based systems**:

    ```bash
    sudo apt install mpv
    ```

    For **Mac** (Homebrew):

    ```bash
    brew install mpv
    ```

### Usage

1. Run the tool:

    ```bash
    python3 yt-cli.py
    ```

2. Enter your search query (e.g., `How to code in Python`).

3. Select a video to play by number.

4. The video will start playing directly in your terminal!

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
