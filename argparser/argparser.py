import argparse

class ArgumentParser(argparse.ArgumentParser):
  def __init__(self, *args, **kwargs):
    
    super().__init__(*args, **kwargs)
  
    self.add_argument(
      '--currency',
      type=str,
      help='currency name',
    )
    self.add_argument(
      '--days',
      type=int,
      help='days of record',
    )

