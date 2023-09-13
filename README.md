# MatchingCVstoJDs

[![GitHub license](https://img.shields.io/github/license/YourUsername/YourRepository)](https://github.com/YourUsername/YourRepository/blob/master/LICENSE)

## Description

Resume-Matcher is a Python script that compares a resume (CV) in PDF format with a set of job descriptions (JDs) stored in a CSV file. It calculates a "match percentage" between the CV and each JD based on cosine similarity of the term frequency vectors.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Libraries: PyPDF2, pdfplumber, scikit-learn (sklearn)

## Installation

To install the required libraries, you can use pip:

```bash
pip install PyPDF2 pdfplumber scikit-learn
