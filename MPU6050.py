import smbus
import time

# MPU6050 registers and addresses
DEVICE_ADDRESS = 0x68
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

# PID parameters
setpoint = 0.0
Kp = 2.0
Ki = 0.5
Kd = 1.0

# Initialize I2C bus
bus = smbus.SMBus(1)

# Read raw sensor data
def read_raw_data(addr):
    high_byte = bus.read_byte_data(DEVICE_ADDRESS, addr)
    low_byte = bus.read_byte_data(DEVICE_ADDRESS, addr + 1)
    value = (high_byte << 8) + low_byte
    return value

# Read accelerometer data
def read_accel_data():
    x = read_raw_data(ACCEL_XOUT_H)
    y = read_raw_data(ACCEL_XOUT_H + 2)
    z = read_raw_data(ACCEL_XOUT_H + 4)
    return x, y, z

# PID controller function
def pid_controller():
    prev_error = 0.0
    integral = 0.0

    while True:
        # Read accelerometer data
        accel_x, _, _ = read_accel_data()

        # Calculate error
        error = setpoint - accel_x

        # Proportional term
        p_term = Kp * error

        # Integral term
        integral += Ki * error

        # Derivative term
        derivative = Kd * (error - prev_error)

        # Calculate PID output
        output = p_term + integral + derivative

        # Update previous error
        prev_error = error

        # Apply PID output to control the system
        # (e.g., adjust motor speed, servo position, etc.)
        print(read_accel_data())
        time.sleep(0.01)  # Adjust the sleep time as needed

# Run the PID controller
pid_controller()
