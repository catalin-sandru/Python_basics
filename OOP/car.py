class Car:
  # top_speed = 100
  # warnings = []
  def __init__(self, starting_top_speed=100):
    self.top_speed = starting_top_speed
    self.warnings = []

  def __repr__(self):
    print('printing')
    return 'top speed {}, Warnings {}'.format(self.top_speed, len(self.warnings))

  def add_warning(self, warning_text):
    if len(warning_text) > 0:
      self.warnings.append(warning_text)

  def drive(self):
    print('I am driving at {} '.format(self.top_speed))

car1 = Car()
car1.drive()

car1.add_warning('new warning')
print(car1)

car2 = Car(200)
car2.drive()
print(car2.warnings)


car3 = Car(250)
car3.drive()
print(car3.warnings)
