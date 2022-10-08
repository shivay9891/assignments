{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOzUaV4S7RUxGTBBl3jP+Mg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivay9891/assignments/blob/main/checkprime.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write program for check prime or not"
      ],
      "metadata": {
        "id": "GZNcQzlvh8QW"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "r_pIbZO7hIy5"
      },
      "outputs": [],
      "source": [
        "def prime(n):\n",
        "  if n==0:\n",
        "    print(f'{n} is neither prime nor not prime')\n",
        "  elif n==1:\n",
        "    print(f'{n} is neither prime nor not prime')\n",
        "  elif n==2:\n",
        "    print(f'{n} is prime')\n",
        "  elif n==3:\n",
        "    print(f'{n} is prime')\n",
        "  elif n==5:\n",
        "    print(f'{n} is prime')\n",
        "  elif n==7:\n",
        "    print(f'{n} is prime')\n",
        "  elif n%2==0:\n",
        "    print(f'{n} is not prime')\n",
        "  elif n%3==0:\n",
        "    print(f'{n} is not prime')\n",
        "  elif n%5==0:\n",
        "    print(f'{n} is not prime')\n",
        "  elif n%7==0:\n",
        "    print(f'{n} is not prime')\n",
        "  else:\n",
        "    print(f'{n} is prime')\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prime(2)\n",
        "prime(3)\n",
        "prime(5)\n",
        "prime(7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Fkm_hhfh7SD",
        "outputId": "c455bdbf-75fd-4d24-f373-9d0731e3fc24"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 is prime\n",
            "3 is prime\n",
            "5 is prime\n",
            "7 is prime\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=int(input())\n",
        "prime(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mXesqlI2iey4",
        "outputId": "b4795ce2-5923-41e7-af54-73702eec54a6"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "10 is not prime\n"
          ]
        }
      ]
    }
  ]
}