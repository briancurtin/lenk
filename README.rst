Lenk
====

Are you tired of those pesky ``KeyError`` exceptions popping up in your
programs? Do you need certain keys planted in your dictionaries?
Do you just want to get away with it all?

Inspired by Manitowoc County Sheriff's Lieutenant James Lenk, ``Lenk``
is a dictionary-like class that plants values for any key you want
to look for. It comes with one key planted by default.

Installation
************

.. code-block::

   pip install lenk

Usage
*****

You use `Lenk` just like any other dictionary.

.. code-block:: python

   >>> from lenk import Lenk
   >>> evidence = Lenk()
   >>> evidence["Toyota Rav4"]
   True
   >>> evidence["something else"]
   'k16uxjcu9wglu25v2kl0'

See? It found that Toyota Rav4 key no problem! It also finds any other
key you'd want to look for.

About
*****

Manitowoc County Sheriff's Lieutenant James Lenk is a bad person.

.. image:: http://i.imgur.com/EHCNSYV.jpg
