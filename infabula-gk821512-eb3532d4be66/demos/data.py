"""
lening
"""
data = {
    'loans':[
               {'type': 'kortstondig',
                'bedrag': 56.7,
                'hash': '44324gfff43242'
               },
    ],
    'person': [
         {'name': 'Henk',
          'status': 'gehuwd',
          'hash': '432798eee43274329'},
         {'name': 'Ans',
          'status': 'gehuwd',
          'hash': '432597e98473924'},
     ]
}

job1 = Etl()
jobs = [job1, job2, job3]
for job in jobs:
    job.run()
