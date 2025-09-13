# xwing_airshow_mini.py

import time, math, random

W, H = 62, 22       # canvas size
N = 12              # number of jets
STEP = 0.7          # movement per tick (bigger = faster)
PAUSE = 18          # frames to hold each pose

class Ship:
    def __init__(self):
        self.x = random.uniform(2, W-3)
        self.y = random.uniform(2, H-3)
        self.g = "🛩️"
    def step(self, tx, ty):
        dx, dy = tx - self.x, ty - self.y
        d = math.hypot(dx, dy)
        if d < 0.02: return True
        a = min(1.0, STEP / d)
        self.x += dx * a; self.y += dy * a
        return False

# --- formations (all return list[(x,y)] of length n) ------------------------

def line(n, w, h):
    y = h/2; gap = (w-4)/(n+1)
    return [(2+(i+1)*gap, y) for i in range(n)]

def vee(n, w, h):
    cx, cy, span = w/2, h/2 - 1, min(w,h)*0.45
    mid = (n-1)/2
    return [(cx + (i-mid)*(span/n), cy + abs(i-mid)*(span/(n*1.6)))\
            for i in range(n)]

def circle(n, w, h):
    cx, cy, r = w/2, h/2, min(w,h)*0.32
    return [(cx + r*math.cos(2*math.pi*i/n), cy + r*math.sin(2*math.pi*i/n))\
            for i in range(n)]

def diamond(n, w, h):
    cx, cy, r = w/2, h/2, min(w,h)*0.36
    out=[]
    for i in range(n):
        a = 2*math.pi*i/n; c, s = math.cos(a), math.sin(a)
        d = abs(c)+abs(s)+1e-9
        out.append((cx + r*(c/d), cy + r*(s/d)))
    return out

def xwing(n, w, h):
    m=2.5; x1=(m,m); x2=(w-m,h-m); y1=(m,h-m); y2=(w-m,m)
    k1=(n+1)//2; k2=n-k1
    def seg(a,b,k):
        ax,ay=a; bx,by=b
        return [(ax+(i+1)/(k+1)*(bx-ax), ay+(i+1)/(k+1)*(by-ay))\
                for i in range(k)]
    d1, d2 = seg(x1,x2,k1), seg(y1,y2,k2)
    out=[]; L=max(k1,k2)
    for i in range(L):
        if i<k1: out.append(d1[i])
        if i<k2: out.append(d2[i])
    return out[:n]

def mirror(form):
    def m(n,w,h): return [(w-x,y) for (x,y) in form(n,w,h)]
    return m



# --- drawing ----------------------------------------------------------------

def draw(ships):
    grid = [[" "]*W for _ in range(H)]
    for s in ships:
        x = max(0, min(W-1, int(round(s.x))))
        y = max(0, min(H-1, int(round(s.y))))
        grid[y][x] = s.g
    print("\x1b[2J\x1b[H", end="")     # clear + home
    print("X-Wing Aerobatic Display — Line → V → Diamond → X → Mirror → Circle"
          "(Ctrl+C to exit)")
    print("\n".join("".join(row) for row in grid))

# --- show loop ---------------------------------------------------------------
if __name__ == "__main__":
    ships = [Ship() for _ in range(N)]
    forms = [line, vee, diamond, xwing, mirror(vee), circle]

    try:
        idx = 0
        while True:
            targets = forms[idx](N, W, H)
            # fly to the new formation
            while True:
                done = True
                for s, (tx,ty) in zip(ships, targets):
                    done &= s.step(tx,ty)
                draw(ships); time.sleep(0.03)
                if done: break
            # hold the pose briefly
            for _ in range(PAUSE):
                draw(ships); time.sleep(0.03)
            idx = (idx + 1) % len(forms)
    except KeyboardInterrupt:
        print("\nShow complete.")
