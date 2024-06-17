from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import tk

root = Tk()
root.title("Draw Charts")
root.geometry("500x400")
root.configure(background="#8fa3c2")


def draw_stripe():
    x = [1, 2, 3, 4]
    y = [1, 5, 8, 18]
    fig, ax = plt.subplots()

    plt.plot(x, y, 'g+')
    fig.savefig("stripe.png", dpi=300)

    # plt.show()


def draw_histogram():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(1000)
    fig, ax = plt.subplots()

    # print(f"x={len(x)}")
    plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
    plt.xlabel("Number people")
    plt.ylabel("Probability")
    plt.title("Histogram of probability of people coming tomorrow")

    # plt.text(60, .025, )
    plt.grid(True)
    fig.savefig("histo.jpg")
    # plt.show()


btn_strip = Button(root, text="Draw Stripe", command=draw_stripe)
btn_strip.pack()

btn_hito = Button(root, text="Draw Histogram", command=draw_histogram)
btn_hito.pack()

root.mainloop()
