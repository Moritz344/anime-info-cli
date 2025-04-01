# Anime Info CLI

A simple CLI application to fetch information such as title, genre, or ranking for any anime.


## 🚀 Installation & Usage

</details>
<details>
<summary>Video</summary>
  
https://github.com/user-attachments/assets/4c241fd9-93d8-40f0-9696-188e0bc4cea2




</details>


### 🔧 Requirements
- **Python 3** must be installed
- **Git**
- termcolor
- rich
-requests

### Easy Setup (Global Access)

```bash
git clone https://github.com/Moritz344/anime-info-cli.git
cd anime-info-cli/src
```

To run the application from anywhere, set it up as a global command:

```bash
echo -e '#!/bin/bash\npython3 $(pwd)/main.py "$@"' > /usr/local/bin/anime-info
chmod +x /usr/local/bin/anime-info
```


Now, you can simply run:
```bash
anime-info
```

from anywhere in the terminal.

#### Deinstall
```bash
sudo rm /usr/local/bin/anime-info
```


### 📥 Manually
```bash
git clone https://github.com/Moritz344/anime-info-cli.git
cd anime-info-cli/src
python3 main.py
```

# Upcoming
I plan to actively develop this project, so expect new features and improvements in the future.


# Author
- Moritz344
