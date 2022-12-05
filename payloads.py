# Payloads based on email from Auxcis 29/11/2022

# Print RFID label
printMessage = '{ "SerialNr" : "123456789", "Location" : "Start", "Type" : "Print", "Timestamp" : 1669732272}'

# Auxis system sending RFID read message
readMessageEntry = '{ "SerialNr" : "123", "Location" : "Point1", "Type" : "Entry", "Timestamp" : 1669732272}'
readMessageUpdate = '{ "SerialNr" : "123", "Location" : "Point1", "Type" : "Update", "Timestamp" : 1669732372}'
readMessageExit = '{ "SerialNr" : "123", "Location" : "Point1", "Type" : "Exit", "Timestamp" : 166973472}'

# Auxis system sending barcode read message
barcodeReadMessage = '{ "SerialNr" : "123456789", "BarCode" : "Start", "Location" : "Point2", "Type" : "Print", "Timestamp" : 1669732272}'