let xhr = new XMLHttpRequest();

xhr.open("POST", "https://reqbin.com/echo/post/json");

let data = {
  "Id": 78912,
  "Customer": "Jason Sweet",
};

xhr.onload = () => console.log(xhr.status);

xhr.send(data);
