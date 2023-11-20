import qrcode

student_id = [221,222,223,224,225,226,227,228,229,230]

for id in student_id:
    generate_qr_code = qrcode.make(str(id))
    generate_qr_code.save(f"resources/qr-code-gen/image{id}.png")