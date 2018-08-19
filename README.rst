Pylarization
============

About
-----
Pylarization is a Python module that aids in processing light
polarization states. For given method of polarization description it can 
calculate all parameters of a polarization ellipse.

Installation
------------

The following should do, as pylarization does not have any
platform-specific dependancies.

.. code-block:: sh

   pip install pylarization

Usage
-----

Polarization Ellipse
~~~~~~~~~~~~~~~~~~~~

PolarizationEllipse is the base class for all classes describing different 
methods of describing the state of polarization.

To create an instance it is necessary to supply light amplitudes along
the X and Y axes and the phase difference between the amplitudes.

.. code-block:: python

   light = PolarizationEllipse(0.445, 0.89, 1.57)


Vectors
~~~~~~~

Jones Vector
^^^^^^^^^^^^

.. code-block:: python

   light = JonesVector(0.445, 0.89j)

Stokes Vector
^^^^^^^^^^^^^

.. code-block:: python

   light = StokesVector(1, 0.6, 0, 0.8)

Matrices
~~~~~~~~

Jonex Matrix
^^^^^^^^^^^^

.. code-block:: python

   matrix_values = numpy.matrix([[1, 0], [0, -1j]])
   light = JonesMatrix(matrix_values) *  JonesVector(1, -1j)
   light.vector
   matrix([[ 1.+0.j],
           [-1.+0.j]])

Mueller Matrix
^^^^^^^^^^^^^^

.. code-block::

   matrix_values = numpy.matrix([[0.5, 0.5, 0, 0], [0.5, 0.5, 0, 0], [0 , 0, 0, 0], [0 , 0, 0, 0]])
   light = MuellerMatrix(matrix_values) *  StokesVector(1, 0, 0, 0)
   light.vector
   matrix([[0.5],
           [0.5],
           [0. ],
           [0. ]])

Coherency Matrix
^^^^^^^^^^^^^^^^

Sources
-------

Florian Ratajczak, Optyka Ośrodków Anizotropowych, Wydawnictwo Naukowe PWN, Warszawa, 1994

Eugene Hecht, Optyka, PWN, Warszawa, 2012

Harland G. Tompkins, Eugene A. Irene, Handbook of Ellipsometry, William Andrew, Inc., Norwich, New York, 2005

http://kestrel.nmt.edu/~mce/Polarization.pdf

https://spie.org/publications/fg05_p07-09_polarization_ellipse?SSO=1

http://orca.phys.uvic.ca/~tatum/physopt/physopt4.pdf

https://arxiv.org/pdf/1401.1911.pdf

http://www.waves.utoronto.ca/prof/svhum/ece422/notes/03-polarization.pdf

http://www.ece.mcmaster.ca/faculty/nikolova/antenna_dload/current_lectures/L05_Polar.pdf

http://www.eecs.ucf.edu/~tomwu/course/eel6482/notes/12%20Polarization%202.pdf

http://www.diss.fu-berlin.de/diss/servlets/MCRFileNodeServlet/FUDISS_derivate_000000002688/04_chapter2.pdf

http://orca.phys.uvic.ca/~tatum/celmechs/celm2.pdf
