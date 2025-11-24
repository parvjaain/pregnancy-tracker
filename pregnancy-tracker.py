import datetime as d
import json as j

b = {
    1: {"s": "poppy seed", "t": "Take folic acid to support healthy development.", "n": "Leafy vegetables like spinach, kale, and broccoli.", "w": "0-1 kg"},
    12: {"s": "lime", "t": "Avoid raw fish and unpasteurized foods.", "n": "Protein-rich foods: eggs, lean meat, beans.", "w": "1-2 kg"},
    20: {"s": "banana", "t": "Stay hydrated and monitor your energy levels.", "n": "Fruits, whole grains, and dairy.", "w": "5-6 kg"},
    28: {"s": "eggplant", "t": "Exercise gently and avoid strenuous activity.", "n": "Calcium-rich foods like milk, cheese, yogurt.", "w": "7-9 kg"},
    36: {"s": "papaya", "t": "Prepare for labor, attend prenatal classes.", "n": "Iron-rich foods: spinach, lentils, red meat.", "w": "10-12 kg"},
    40: {"s": "pumpkin", "t": "Stay calm, ensure rest and relaxation.", "n": "Balanced diet with all essential nutrients.", "w": "12-14 kg"}
}

m = {
    12: "First ultrasound scan - see your baby’s growth.",
    16: "Routine blood test - check your health parameters.",
    20: "Detailed ultrasound scan - monitor baby’s anatomy.",
    28: "Tetanus booster vaccination - protect you and baby.",
    36: "Prepare for delivery - pack hospital bag and final checkups."
}

t = {
    1: "Trimester 1: Focus on vitamins, avoid stress, gentle exercise, hydrate well, and get plenty of rest.",
    2: "Trimester 2: Track baby growth, maintain healthy diet, moderate exercise, and attend prenatal checkups.",
    3: "Trimester 3: Monitor baby kicks, practice breathing exercises, plan delivery, and maintain calm mindset."
}

def a(s):
    x = d.timedelta(weeks=40)
    k = s + x
    return k

def v(w):
    if w <= 13:
        return 1
    elif w <= 27:
        return 2
    else:
        return 3

def x(w):
    q = []
    for y in b:
        if y <= w:
            q.append(y)
    if len(q) > 0:
        z = max(q)
        return z
    else:
        return 1

def y(ed):
    c = ed - d.datetime.now()
    z = c.days
    return z

def z(d, f="pp.json"):
    try:
        op = []
        f1 = open(f, "r")
        op = j.load(f1)
        f1.close()
    except:
        op = []
    op.append(d)
    f1 = open(f, "w")
    j.dump(op, f1, indent=4)
    f1.close()

q = input("Enter current pregnancy week (1-40): ")
w = int(q)
q2 = input("Enter first day of last menstrual period (YYYY-MM-DD): ")
s = d.datetime.strptime(q2, "%Y-%m-%d")
q3 = input("Current weight in kg: ")
c = float(q3)
q4 = input("Any symptoms this week? (comma separated): ")
syli = []
if q4:
    syli = []
    for u in q4.split(","):
        syli.append(u.strip())
else:
    syli = []

qw = x(w)
ed = a(s)
dl = y(ed)
tr = v(w)
upm = []
for r in m:
    if r >= w:
        upm.append(r)

print("\n==== PREGNANCY WEEK SUMMARY ====")
print("Week:", w)
print("Baby size:", b[qw]["s"])
print("Safety tip:", b[qw]["t"])
print("Nutrition:", b[qw]["n"])
print("Weight gain avg:", b[qw]["w"])
print("Trimester note:", t[tr])
print("Expected delivery:", ed.strftime("%d %b %Y"))
print("Days left:", dl, "days")

print("\n==== UPCOMING MILESTONES ====")
if len(upm) > 0:
    for r in upm:
        print("Week", r, ":", m[r])
else:
    print("No milestones.")

print("\n==== SYMPTOMS TRACKER ====")
if len(syli) > 0:
    for s_ in syli:
        print("-", s_)
else:
    print("No symptoms.")

print("\nRemember: Each week baby grows, your body adapts. Hydrate, eat well, rest.")
print("Track daily, tell doctor any concerns.")
print("Balance food: fruits, veg, protein, calcium, iron.")
print("Gentle walk/exercise ok, no heavy lift.")
print("Watch weight gain.")
print("Feel fetal moves, note change.")
print("Get ready for checkups, vaccines, listen to doctor.")
print("Mental health: relax, stay positive.")
print("Log/journal progress weekly.")
print("Progress saves for future.")

p = {"w": w, "date": str(d.datetime.now().date()), "cw": c, "sy": syli}
z(p)

print("\nProgress saved. Stay healthy! End of summary. Enjoy your journey!")
