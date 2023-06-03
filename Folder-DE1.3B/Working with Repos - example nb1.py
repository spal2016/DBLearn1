# Databricks notebook source
files = dbutils.fs.ls(f"{DA.paths.datasets}/nyctaxi-with-zipcodes/data")
display(files)

