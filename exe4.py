import os
import sys
def install_or_remove_packages(): iOrR = ""
while iOrR != "I" and iOrR != "R":
    print("Vous souhaitez installer ou supprimer des packages? (I/R)")
    iOrR = input().upper()
    if iOrR == "I":iOrR = "install"
    elif iOrR == "R":iOrR = "remove"