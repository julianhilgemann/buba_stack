---

# 🧠 Git & GitHub Cheatsheet for Developers & Analysts

A compact guide to help you **understand Git**, **track your code changes**, and **push your work to GitHub**.

---

## 📌 What is Git?

**Git** is a version control system that helps you:
- Track changes to your code
- Revert to earlier versions
- Collaborate with others
- Avoid "final_final_version3.py" syndrome 😅

> Think of Git as a **time machine** for your project.

---

## 📌 What is GitHub?

**GitHub** is a cloud-based hosting service for Git repositories. It:
- Stores your code remotely
- Lets you share your projects
- Enables collaboration with version control
- Acts as a public or private portfolio

> Git = the tool. GitHub = the website that hosts your Git repositories.

---

## 🔑 Core Concepts

| Term             | What It Means                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **Repository**   | A folder tracked by Git (local or on GitHub)                                 |
| **Commit**       | A snapshot of your code (with a message)                                     |
| **Branch**       | A parallel version of your project (for experiments or features)             |
| **Merge**        | Combines two branches                                                        |
| **Remote**       | A GitHub-hosted version of your local repo                                   |
| **Clone**        | Download a GitHub repo locally                                                |
| **Push**         | Send your changes to GitHub                                                   |
| **Pull**         | Get the latest changes from GitHub                                            |
| **.gitignore**   | Tells Git which files to ignore (like `venv/`, `.env`, etc.)                  |

---

## 🚀 Basic Git Workflow (Local ➡️ GitHub)

```bash
# Start tracking a folder
git init

# Add files to staging (to be committed)
git add .

# Commit with a message
git commit -m "Initial commit"

# Link to GitHub repo
git remote add origin https://github.com/username/repo-name.git

# Push to GitHub (create main branch if needed)
git branch -M main
git push -u origin main
```

---

## 🛠️ Everyday Commands

### ✅ Local Work

```bash
git status               # See what's changed
git diff                 # View changes in detail
git add <file>           # Stage specific file
git commit -m "msg"      # Save changes with message
```

### 🌐 Remote Interaction

```bash
git remote -v            # View linked remotes
git push                 # Push to GitHub
git pull                 # Get latest from GitHub
git clone <url>          # Copy repo from GitHub
```

### 🌱 Branching

```bash
git branch               # List branches
git checkout -b feature  # Create + switch to branch
git checkout main        # Switch back to main
git merge feature        # Merge feature into main
```

---

## 🧹 Undoing Stuff

```bash
git restore <file>               # Undo changes to file
git reset HEAD <file>            # Unstage file
git log                          # View commit history
git revert <commit_hash>         # Undo specific commit (safely)
```

---

## 📄 Example .gitignore (for Python/BI Projects)

```gitignore
# Ignore virtual environments
venv/

# Ignore cache and bytecode
__pycache__/
*.pyc

# Ignore secrets or config
.env

# Ignore data dumps or exports
*.csv
*.xlsx
```

---

## 🤖 VSCode + Git Tips

- Use **Source Control tab** to visually manage changes.
- You can stage, commit, and push directly from the UI.
- Install the **GitLens extension** for advanced Git history and insight.

---

## 🔗 GitHub Tips

- `README.md`: Add one to explain your project
- `LICENSE`: Optional, but important for open source
- **Commits are public portfolio signals** — use clear messages!
- Private repos available with free GitHub accounts too

---

## 📚 Suggested Learning Progression

1. `git init`, `git add`, `git commit`  
2. `git remote add`, `git push`  
3. `git clone`, `git pull`, `git branch`, `git merge`  
4. Learn `.gitignore` and undo commands  
5. Practice using branches for new features or experiments

---

## 🧠 Pro Tips

- Commit early and often with clear messages.
- Always pull before you push to avoid conflicts.
- Use branches to isolate work without breaking main.
- Keep `.gitignore` clean to avoid accidentally pushing sensitive files.

---