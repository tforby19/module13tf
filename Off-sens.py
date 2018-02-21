turn_off = motor_stop

motorR= 0
motorL= 1
sensor_pin= 16

While RPL.digitalRead(sensor_pin)== 1:
  RPL.servoWrite(motorR, 1000)
  RPL.servoWrite(motorL, 1000)

Else:
   RPL.servoWrite(motorR, 0)
   RPL.servoWrite(motorL, 0)

#this should turn my motor off based on the sensor reading in the front, if not i failed 
