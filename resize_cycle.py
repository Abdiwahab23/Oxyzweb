import sys

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block
old_css = '''/* ======================== */
/* 5D Cycle                 */
/* ======================== */
.cycle-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 60px auto;
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cycle-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 440px;
  height: 440px;
  transform: translate(-50%, -50%);
  z-index: 0;
  animation: rotateRing 40s linear infinite;
}
@keyframes rotateRing {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}
.cycle-center {
  position: absolute;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: var(--white);
  border: 2px solid var(--gold);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 2;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.cycle-center .cycle-number {
  font-size: 6rem;
  font-weight: 300;
  color: var(--text-dark);
  line-height: 1;
  font-family: var(--font-primary);
}
.cycle-center .cycle-text {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: center;
  margin-top: -10px;
}
.cycle-node {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 140px;
  height: 140px;
  margin-top: -70px;
  margin-left: -70px;
  --radius: 220px;
  transform: rotate(var(--angle)) translate(var(--radius)) rotate(calc(-1 * var(--angle)));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--white);
  border-radius: 20px;
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  z-index: 1;
}
.cycle-node:hover {
  transform: rotate(var(--angle)) translate(var(--radius)) rotate(calc(-1 * var(--angle))) scale(1.1);
  border-color: var(--gold);
  box-shadow: 0 15px 35px rgba(212, 175, 55, 0.15);
}
.cycle-icon {
  font-size: 2.5rem;
  color: var(--gold);
  margin-bottom: 12px;
}
.cycle-label {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-dark);
  text-transform: uppercase;
  letter-spacing: 1px;
}
.cycle-label span {
  font-size: 1.4rem;
  color: var(--gold);
  font-style: italic;
}'''

new_css = '''/* ======================== */
/* 5D Cycle                 */
/* ======================== */
.cycle-container {
  position: relative;
  width: 100%;
  max-width: 420px;
  margin: 40px auto 60px auto;
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cycle-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 340px;
  height: 340px;
  transform: translate(-50%, -50%);
  z-index: 0;
  animation: rotateRing 40s linear infinite;
}
@keyframes rotateRing {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}
.cycle-center {
  position: absolute;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: var(--white);
  border: 2px solid var(--gold);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 2;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.cycle-center .cycle-number {
  font-size: 4.5rem;
  font-weight: 300;
  color: var(--text-dark);
  line-height: 1;
  font-family: var(--font-primary);
}
.cycle-center .cycle-text {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: center;
  margin-top: -5px;
}
.cycle-node {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 110px;
  height: 110px;
  margin-top: -55px;
  margin-left: -55px;
  --radius: 180px;
  transform: rotate(var(--angle)) translate(var(--radius)) rotate(calc(-1 * var(--angle)));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--white);
  border-radius: 16px;
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  z-index: 1;
}
.cycle-node:hover {
  transform: rotate(var(--angle)) translate(var(--radius)) rotate(calc(-1 * var(--angle))) scale(1.1);
  border-color: var(--gold);
  box-shadow: 0 15px 35px rgba(212, 175, 55, 0.15);
}
.cycle-icon {
  font-size: 1.8rem;
  color: var(--gold);
  margin-bottom: 8px;
}
.cycle-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-dark);
  text-transform: uppercase;
  letter-spacing: 1px;
}
.cycle-label span {
  font-size: 1.1rem;
  color: var(--gold);
  font-style: italic;
}'''

if old_css in content:
    content = content.replace(old_css, new_css)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced exact string.")
else:
    # Use regex
    import re
    # We will just replace everything from '/* ======================== */\n/* 5D Cycle                 */' up to '@media (max-width: 768px) {'
    pattern = re.compile(r'/\* ======================== \*/\s*/\* 5D Cycle                 \*/\s*/\* ======================== \*/.*?@media \(max-width: 768px\) \{', re.DOTALL)
    match = pattern.search(content)
    if match:
        content = content[:match.start()] + new_css + '\n\n@media (max-width: 768px) {' + content[match.end():]
        with open('css/style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Replaced using regex.")
    else:
        print("Could not find the target CSS block.")
