import qrcode

student_id = "1234567891"
generate_qr_code = qrcode.make(student_id)
generate_qr_code.save("resources/qr-code-gen/image02.png")