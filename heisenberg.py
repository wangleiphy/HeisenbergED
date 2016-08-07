import pyalps

#prepare the input parameters
parms = [{ 
          'LATTICE'                   : "chain lattice", 
          'MODEL'                     : "spin",
          'local_S'                   :  0.5,
          'J'                         :  1,
          'L'                         :  16,
          'CONSERVED_QUANTUMNUMBERS'  :  'Sz',
          'Sz_total'                  :  0, 
 	      'TRANSLATION_SYMMETRY'      :  'true',
          'NUMBER_EIGENVALUES'        :  5,
          'TOTAL_MOMENTUM'            :  "0"
        }]

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('heisenberg',parms)
res = pyalps.runApplication('sparsediag',input_file)
