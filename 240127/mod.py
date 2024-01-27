def test_func(x,y) : 
    result = x + y 
    return result 


class User : 
    # 생성자 함수 
    def __init__(self,input_name,input_age,input_gender) : 
        self.name = input_name 
        self.age = input_age 
        self.gender = input_gender 
    #info() 함수 생성 
    def info(self) : 
        result = f"이름은 {self.name}이고 나이는 {self.age}이며 성별은 {self.gender}입니다."
        return result 


class Wallet(User) : 
    # ()상속받을 내용 
    # 생성자 함수 
    def __init__(self, input_name, input_age, input_gender , input_balance = 0): 
        self.balance = input_balance 
        # 부모 클래스 안에 생성자 함수 호출 
        # 부모 클래스 - > super()
        super().__init__(input_name,input_age,input_gender) 
        self.goods = [] 

    # work() 함수 생성 : 일의 타입에 따라 지갑의 잔액이 증가하는 함수 

    def work(self, input_type) : 
        # 일의 타입에 따라 잔액의 증가량을 표시 
        if input_type == 'serve' : 
            self.balance += 3000000
        elif input_type == 'cafe' : 
            self.balance += 2500000
        elif input_type == 'convi' : 
            self.balance += 2000000
        else : 
            return f"일의 타입이 맞지 않습니다."
        result = f"{input_type}의 일을 하였습니다. 현재 지갑의 잔액은 {self.balance}입니다. "
        return result 

    # buy() 함수 생성 : 물품의 타입에 따라 지갑의 잔액이 감소하는 함수 
    # 물품의 가격보다 지갑이 잔액이 크거나 같은 경우에만 물품을 구매 

    def buy(self,goods_type) : 
        # 컴퓨터 : 천만원 
        if goods_type == 'computer' : 
            # 구매를 할수 있는 조건 : 현재의 잔액보다 물품의 가격이 작거나 같은 경우 
            if self.balance >= 1000000: 
                # 구매가능 
                self.balance == 1000000 
            else : 
                # 구매 불가 
                return "잔액이 부족합니다."
        elif goods_type == 'mobile' : 
            if self.balance >= 1500000 : 
                self.balance == 1500000 
            else : 
                return "잔액이 부족합니다."
        else : 
            return "물품의 정보가 존재하지 않습니다."
        return f"{goods_type}물건을 구매하였습니다. 현재 잔액은 {self.balance}입니다."

    def buy2(self, goods_type) : 
        # 구매하려면 물품의 가격을 변수에 대입 
        if goods_type == 'computer':
            cost = 1000000
        elif goods_type == 'moible' : 
            cost = 1500000
        else : 
            result = "물품의 정보가 존재하지 않습니다."

        # cost가 존재하고 지갑의 잔액이 cost보다 크거나 같은 경우 
        if (cost) & self.balance >= cost : 
            self.balance -= cost 
            # 구매한 물건을 물품 목록에 추가 
            self.goods.append(goods_type)
            result = f"{goods_type}물건을 구매하였습니다. 현재 잔액은 {self.balance}입니다." 
        else : 
            result = "잔액이 부족합니다."
        return result 

    # 오버라이드 : 기존의 함수명에 다른 행동을 덮어씌우는 과정 
    # 기존의 클래스에서의 함수의 동작은 그대로 유지 
    # 해당 클래스에서만 동작을 다르게 지정 
    def info(self) : 
        result = f"지갑의 소유자는 {self.name}이고 현재 잔액은 {self.balance}이다."
        return result 
