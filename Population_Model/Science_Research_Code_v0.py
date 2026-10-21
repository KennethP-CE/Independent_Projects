import math
import matplotlib.pyplot as plt
t = 1
AxisX = 0
AxisXr = 0
def run_equation(N1, B1, P1, N2, P2, M2, TX, AxisX, AxisXr):
    while TX > -1:
        if N1 < 1:
            N1 = 0
        if N2 < 1:
            N2 = 0
        T2 = 1200
        rN1 = round(N1, 0)
        rN2 = round(N2, 0)
        timeXr.append(AxisXr)
        prey.append(rN1)
        predator.append(rN2)
        while T2 > 0:
            dN1 = (1/1200)*(B1*N1-P1*N1*N2)
            dN2 = (1/1200)*(P2*N1*N2-M2*N2)
            N1 = round(N1 + dN1, 9)
            N2 = round(N2 + dN2, 9)
            if T2 % 100 == 0:
                timeX.append(AxisX)
                preyG.append(N1)
                predatorG.append(N2)
                AxisX = AxisX + 1
            T2 = T2-1
        N1 = round(N1, 2)
        N2 = round(N2, 2)
        TX = TX-1
        AxisXr = AxisXr + 1

while t == 1:
    prey = []
    predator = []
    preyG = []
    predatorG = []
    timeX = []
    timeXr = []
    tN1 = round(float(input("What is the starting prey population size? ")), 0)
    tB1 = float(input("What is the prey's birthrate? "))
    tP1 = float(input("What is the probability for a predator to hunt prey? "))
    tN2 = round(float(input("What is the starting predator population size? ")), 0)
    tP2 = float(input("What is the probability that the predator's population size will grow by the prey? "))
    tM2 = float(input("What is the predator's mortality rate? "))
    tTX = round(float(input("How many steps should the simulation encompass? ")), 0)
    N1 = tN1
    B1 = tB1
    P1 = tP1
    N2 = tN2
    P2 = tP2
    M2 = tM2
    TX = tTX


    run_equation(N1, B1, P1, N2, P2, M2, TX, AxisX, AxisXr)
    print("preyG: ", preyG)
    print("predatorG: ", predatorG)
    print("prey: ", prey)
    print("predator: ", predator)

    # Plot both data sets
    plt.plot(timeXr, prey, marker='', label="Prey")
    plt.plot(timeXr, predator, marker='', label="Predator")

    # Labels and title
    plt.xlabel("time (years)")
    plt.ylabel("populations")
    plt.title("Population vs. Time")

    # Show legend
    plt.legend()

    # Optional: grid for readability
    plt.grid(True)

    # Display the plot
    plt.show()
    input("Type something to view the next graph: ")

    plt.plot(prey, predator, marker='')   # marker='o' makes each point visible
    plt.xlabel("Prey")
    plt.ylabel("Predator")
    plt.title("Predator vs. Prey Graph")
    plt.grid(True)  # optional but helpful
    plt.show()
    input("Type something to view the next graph: ")
    t = 2