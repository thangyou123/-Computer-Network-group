import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time()*(10**7)) % 0x100000000
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		
		# header[0] = ...
		# ...
		
		# Get the payload from the argument
		# self.payload = ...
		header[0] = (
			header[0] 
			|   version << 6 
			|   padding << 5 
			|   extension << 4
			|   cc
		)

		header[1] = (
			header[1]
			|   marker << 7
			|   pt 
		)

		header[2:3]=[seqnum >> 8,seqnum & 255]
		header[4:8]=[
			(timestamp >> i) & 255 for i in [24,16,8,0]
		]
		header[8:16]=[
			(timestamp >> i) & 255 for i in [24,16,8,0]
		]
		self.header = header
		self.payload = bytes(payload)
		
	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload