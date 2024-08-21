FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CMD ["pytest"]
CMD ["sh", "-c", "python test_add.py && python test_subtract.py && python test_multiply.py && python test_divide.py"]