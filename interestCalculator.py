''' A Tkinter interest calculator program'''

import Tkinter as tk 

fields = ('Annual rate', 'Number of payments', 'Loan principle', 'Monthly payment',
          'Remaining loan')

def monthlyPayment(entries):
    # period rate:
    r = (float(entries['Annual rate'].get()) / 100) / 12
    print('r ', r )
    
    # principal loan
    loan = float(entries['Loan principle'].get())
    n = float(entries['Number of payments'].get())
    remaining_loan = float(entries['Remaining loan'].get())
    q = (1+r)**n
    monthly = r * ((q*loan - remaining_loan)/ (q-1))
    monthly = ("%8.2f" % monthly).strip()
    entries['Monthly payment'].delete(0, tk.END)
    entries['Monthly payment'].insert(0, monthly)
    print("Monthly payment: %f" % float(monthly))

def finalBalance(entries):
    # period rate:
    r = (float(entries['Annual rate'].get()) / 100) / 12
    print('r ', r )
    
    # principal loan
    loan = float(entries['Loan principle'].get())
    n = float(entries['Number of payments'].get())
    monthly = float(entries['Monthly payment'].get())
    remaining_loan = float(entries['Remaining loan'].get())
    q = (1+r)**n
    remaining = q*loan - ((q-1)/r)*monthly
    remaining_loan = ("%8.2f" % remaining).strip()
    entries['Remaining loan'].delete(0, tk.END)
    entries['Remaining loan'].insert(0, monthly)
    print("Remaining loan: %f" % float(remaining))


def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Final Balance',
           command=(lambda e=ents: finalBalance(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Monthly Payment',
           command=(lambda e=ents: monthlyPayment(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
