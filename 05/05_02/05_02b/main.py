from collections import deque

printer_queue = deque()
printer_queue.append("Tickets.pdf")
printer_queue.append("Marketing.docx")
printer_queue.append("proof.png")

while len(printer_queue):
  document = printer_queue.popleft()
  print(f'Printing {document}')