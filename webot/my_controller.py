from controller import Robot

robot = Robot()
time_step = 32
max_speed = 1.57

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
    
left_ir = robot.getDevice('ir2')
left_ir.enable(time_step)
    
right_ir = robot.getDevice('ir1')
right_ir.enable(time_step)

while(-1):
    robot.step(time_step)
    left_ir_value = left_ir.getValue()
    right_ir_value = right_ir.getValue()
        
    print("{} {} ".format(left_ir_value, right_ir_value))
        
    left_speed = max_speed
    right_speed = max_speed
          
    if (left_ir_value > right_ir_value) and (6<left_ir_value<15):
         print("left")
         left_speed = -max_speed
         
    elif (left_ir_value < right_ir_value) and (6<right_ir_value<15):
            print("right")
            right_speed = -max_speed
            
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
