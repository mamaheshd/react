import { ADD_TO_CART } from "../constants/cartConstant";

export const cartReducer=(state={cartItems:[]},action)=>{
    switch(action.type){
        case ADD_TO_CART:
            const item=action.payload
            const isItemExists=state.cartItems.find(i=>i.id === item.id)
            if(isItemExists){
                return{
                    ...state,
                    cartItems:state.cartItems.map(item=>i.id===isItemExists ? item:i)
                }
            }
            else{
                return{
                    ...state,
                    cartItems:[...state.cartItems,item]
                }
            }
        default:
            return {
                ...state
            }
    }
}