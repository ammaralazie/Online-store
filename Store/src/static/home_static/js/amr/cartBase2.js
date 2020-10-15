var updateBtns=document.getElementsByClassName('update-cart1');
console.log(updateBtns.length)
for (var i=0 ;i<updateBtns.length;i++){
updateBtns[i].addEventListener('click',function(){
var productID=this.dataset.product,
    action=this.dataset.action;
if (user==='AnonymousUser'){addCookieItem(productID,action)
}else{

updateUserOrder(productID,action);

}//end if
}//end function listener
)
}//end for 1

function addCookieItem(productID,action){
  console.log('this user is not Authenticated')
  if (action == 'add'){
    if (cart[productID] == undefined){
      cart[productID]={'quantity':1}
      console.log(productID,':',cart[productID])
    }//end if
    else {
      cart[productID]['quantity']+=1
      console.log(cart[productID])
    }//end else

}//end if action add

  if (action == 'remove'){
    cart[productID]['quantity']-=1
    if (  cart[productID]['quantity'] <= 0){delete cart[productID]}
  }//end if remove

  document.cookie='cart='+JSON.stringify(cart)+";domain=;path=/" ;
  location.reload()
}//end function cookie item

function updateUserOrder(productID,action){
  console.log('user is authenticated', 'sendind data ...')

var url='/products/addAndRemovItem/';

fetch(url,{

method:'POST',
headers:{'Content-Type':'apliction/json' , 'X-CSRFToken' :csrftoken} ,
body : JSON.stringify({'productID':productID ,'action':action})

}).then(function(response){

  return response.json();

}//end method response
)
.then(function(data){

  console.log('data',data);
  location.reload()


}//end function data
)
}//end method update user order
