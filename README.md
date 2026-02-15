
# Python Mini Projects Collection

A collection of Python projects including games, utility tools, and GUI applications built for learning and practice.

## Projects Included

### 1. Alarm Clock
A desktop alarm clock application.
- **Features:** Set multiple alarms, snooze functionality, custom alarm sounds
- **Libraries:** `tkinter`, `datetime`, `pygame/playsound`, `threading`

### 2. Hangman Game
Classic word guessing game with text-based interface.
- **Features:** Random word selection, difficulty levels, score tracking
- **Libraries:** `random`, `string`, `os`

### 3. Digital Clock
A real-time digital clock display with GUI interface.
- **Features:** 12/24 hour format, date display, customizable colors
- **Libraries:** `tkinter`, `time`, `datetime`

## Installation

### Clone the Repository
```bash
git clone (https://github.com/ojaspaul123/PYTHON_PROG)
cd python-mini-projects
```

### Install Required Libraries
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pygame
pip install playsound
# tkinter usually comes pre-installed with Python
```

## Requirements

- Python 3.7 or higher
- tkinter (usually comes with Python)
- pygame (for alarm clock sound)
- playsound (alternative for playing sounds)

## Project Structure

```
python-mini-projects/
├── Alarm_Clock/
│   ├── Alarm_Clock.py
│   ├── Premalu.mpeg
│   └── README.md
├── HangmanGame/
│   ├── main.py
│   ├── wordlist.txt
│   └── README.md
├── digital_clock/
│   ├── main_prog.py
│   └── README.md
├── requirements.txt
├── README.md
└── LICENSE
```

## Usage

### Running Alarm Clock
```bash
cd alarm_clock
python alarm_clock.py
```

**How to use:**
1. Launch the application
2. Set the alarm time using the time picker
3. Click "Set Alarm" button
4. The alarm will ring at the specified time

### Running Hangman Game
```bash
cd hangman_game
python hangman.py
```

**How to play:**
1. Run the game
2. Guess letters one at a time
3. Try to complete the word before running out of attempts
4. Each wrong guess adds a part to the hangman

### Running Digital Clock
```bash
cd digital_clock
python digital_clock.py
```

**Features:**
- Displays current time in real-time
- Shows date and day of the week
- Toggle between 12-hour and 24-hour format

## Libraries Used

### GUI Development
- **tkinter** - Creating graphical user interfaces for alarm clock and digital clock
- **tk.messagebox** - Displaying alert messages and dialogs

### Time and Date Management
- **datetime** - Handling date and time operations
- **time** - Time-related functions and delays

### Sound Playback
- **pygame.mixer** - Playing alarm sounds
- **playsound** - Alternative for simple sound playback

### Utility Libraries
- **threading** - Running alarm checks in background
- **random** - Generating random words for hangman
- **string** - String manipulation for hangman game
- **os** - File and system operations

## Requirements.txt

```
pygame>=2.0.0
playsound>=1.2.2
```

## Features

### Alarm Clock
- ✅ Set custom alarm times
- ✅ Multiple alarm support
- ✅ Snooze functionality
- ✅ Custom alarm sounds

### Hangman Game
- ✅ Random word generation
- ✅ Multiple difficulty levels
- ✅ Score tracking
- ✅ Hint system
- ✅ Word categories

### Digital Clock
- ✅ Real-time clock display
- ✅ Date and day display
- ✅ 12/24 hour format toggle
- ✅ Customizable colors and fonts
- ✅ Minimalist design

## Screenshots

*Add screenshots of your projects here*

## Future Enhancements

- [ ] Add more games (Snake, Tic-Tac-Toe, etc.)
- [ ] Improve GUI design with modern themes
- [ ] Add database support for saving user preferences
- [ ] Create calculator application
- [ ] Add weather widget to digital clock
- [ ] Multiplayer support for hangman game

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/NewProject`)
3. Commit your changes (`git commit -m 'Add new project'`)
4. Push to the branch (`git push origin feature/NewProject`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Issue:** Tkinter not found
```bash
# For Ubuntu/Debian
sudo apt-get install python3-tk

# For macOS (usually pre-installed)
brew install python-tk
```

**Issue:** Pygame sound not playing
- Make sure you have audio drivers installed
- Check if the sound file path is correct
- Try using `playsound` as an alternative

**Issue:** Permission denied error
- Run with appropriate permissions
- Check file paths are correct

## Learning Resources

These projects use concepts like:
- Object-Oriented Programming (OOP)
- GUI development with tkinter
- Event handling and callbacks
- Multithreading
- File handling
- Error handling and exceptions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Your Name**
- GitHub: [@yourusername](https://github.com/ojaspaul123)
- Email: ojaspaul123@gmail.com

## Acknowledgments

- Python documentation
- Tkinter tutorial resources
- Open-source community

## Support

If you find this helpful, please ⭐ star the repository!
