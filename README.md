# Item Randomizer for Experiment Sequences

## About

This script generates a randomized event sequence.\
Such a sequence of events is used, for example, in\
**event based EEG experiments**.

For a given set classes, each containing an equal amount\
of items, it shuffles the data.

# How it works

Consider a set of four **categories**, each containing\
**8 Items**. One would like to split the sequence in\
**phases of 20 items**, such that 5 items of each class appear.

Each item is therefore **repeated a total of 5 times**.\
So that each item appears only once per phase.

This results in a **sequence of 160 items** with 8 phases of\
20 items each, with 5 different items from each class.

# Usage

## Install Python

In order to use this script it is necessary to install Python 3.x.\
You can [Download Python ](https://www.python.org/downloads/) from this site.

## Input Item Structure

An input **file with the name "items.csv"** is required.\
Within the file the **items are sorted by class**.\
The **number of items per class** must be the same for all\
classes.

Inside the script the **parameters** for the\
**number of items per class** and the\
**number of repetitions** must be adjusted.

See the example for more information.


# Example

You can find the input items.csv [here]()\
Based on that the output will look like [this]()




### Thanks to the creators of StackEdit!

> Written with [StackEdit](https://stackedit.io/).\
> On-/Offline Live Markdown Editor.
