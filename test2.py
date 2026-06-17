import sys
sys.path.insert(0, '.')
from main import stamp_pdf

import os
jobs = sorted(os.listdir('uploads'))
last = jobs[-1]
pdf = f'uploads/{last}/CAMS GST JUNE (1)-9.pdf'
sig = f'uploads/{last}/WhatsApp Image 2026-05-18 at 14.31.21.jpeg'

try:
    result = stamp_pdf(pdf, 'test_cams2.pdf', sig, 'Aniket Chopra', 'Partner')
    print('Result:', result)
except Exception as e:
    print('Error:', e)
    