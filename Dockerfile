FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# 使用 pytest 進行 CI 測試流程
# CMD ["pytest"] 

# 不使用 pytest 進行 CI 測試流程
CMD sh -c "python test_add.py > logs/test_add_result.log 2>&1 \ && python test_subtract.py > logs/test_subtract_result.log 2>&1 \ &&  python test_multiply.py > logs/test_multiply_result.log 2>&1 \ && python test_divide.py > logs/test_divide_result.log 2>&1"