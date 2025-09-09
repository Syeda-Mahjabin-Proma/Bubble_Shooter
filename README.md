# 🔵 Bubble Shooter (Python OpenGL Game)

## Overview

**Bubble Shooter** is a colorful arcade game built using **Python** and **PyOpenGL**.
Your mission: **Fire bubbles to pop the falling ones before they hit your shooter or escape the screen**!
With random colors, dynamic speeds and only a few lives, every second counts.

---

## 🎮 How to Play

* **Move Shooter**

  * `A` / `Left Arrow` → Move Left
  * `D` / `Right Arrow` → Move Right

* **Shoot a Bubble**

  * `Spacebar` → Launch a yellow bubble upward

* **Objective**

  * Destroy falling bubbles before they collide with your shooter.
  * Avoid missing too many — **3 misses = Game Over**.
  * Colliding with a falling bubble ends the game instantly.

* **On-Screen Buttons**

  * 🔄 **Restart** → Start a new round
  * ⏯ **Play/Pause** → Pause or resume the game
  * ❌ **Exit** → Quit the game

---

## 🕹 Features

* **Randomized Gameplay**

  * Falling bubbles have **random sizes, colors, and speeds** for endless variety.

* **Score System**

  * +1 point for every falling bubble popped.

* **Challenging Mechanics**

  * Limited lives and instant game over on direct collision.

* **Custom Rendering**

  * Uses **Bresenham’s midpoint algorithms** for line and circle drawing.

---

## 📥 Installation & Run

1. **Clone this repository**

   ```bash
   git clone https://github.com/Syeda-Mahjabin-Proma/Bubble_Shooter.git
   cd Bubble_Shooter
   ```

2. **Install dependencies**

   ```bash
   pip install PyOpenGL PyOpenGL_accelerate
   ```

3. **Run the game**

   ```bash
   python bubble_shooter.py
   ```

---

## 🛠 Technologies Used

* **Language:** Python 3.x
* **Graphics Library:** PyOpenGL (GL, GLUT, GLU)
* **Math & Logic:** Collision detection, Bresenham’s midpoint algorithms

---

## 🎥 Demo Video



https://github.com/user-attachments/assets/56d2e1bc-e765-4c30-a9c5-a55464dbe9c2



## 🤝 How to Contribute

1. Fork this repository.
2. Create a branch for your feature:

   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:

   ```bash
   git commit -m "Added feature"
   ```
4. Push your branch:

   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
