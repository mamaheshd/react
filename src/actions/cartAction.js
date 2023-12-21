// import axios from "axios";
import { ADD_TO_CART } from "../constants/cartConstant";
import { API_URL } from "../apiServer";

export const addItemToCart=(id,quantity)=>async(dispatch)=>{
    const {data}= await axios.get(`${API_URL}/${id}`)
    dispatch({
        type:ADD_TO_CART,
        payload:{
            id:data.id,
            name:data.name,
            proce:data.price,
            image:data.image,
            catagory:data.catagory,
            quantity
        }
    })
    localStorage.setItem('cartItem',JSON.stringify(getState().cart.cartItems))
}