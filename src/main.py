from fastapi import FastAPI

from app.utils.tcp import send_async
from app.schemas.can import CANMessage
from app.schemas.can_commands import LocomotiveSpeedCommand, LocomotiveDirectionCommand, LocomotiveFunctionCommand
from app.schemas.can_commands import SystemStopCommand, SystemGoCommand
from app.schemas.can_commands import ParticipantPingCommand
from app.schemas.can_commands import SystemHaltCommand, LocomotiveEmergencyStopCommand, LocomotiveCycleStopCommand

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Testing"}

@app.post("/can")
async def can_message(message: CANMessage):
    await send_async(message.to_bytes())
    return {"send_status": "success"}

@app.post("/api/loc_speed")
async def loc_speed(message: LocomotiveSpeedCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/loc_direction")
async def loc_speed(message: LocomotiveDirectionCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/loc_function")
async def loc_speed(message: LocomotiveFunctionCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/start")
async def system_start(message: SystemGoCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/stop")
async def system_start(message: SystemStopCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/halt")
async def system_start(message: SystemHaltCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/locomotive_emergency_stop")
async def system_start(message: LocomotiveEmergencyStopCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/locomotive_cycle_stop")
async def system_start(message: LocomotiveCycleStopCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}

@app.post("/api/participant_ping")
async def participant_ping(message: ParticipantPingCommand):
    await send_async(message.to_can_message().to_bytes())
    return {"send_status": "success"}