import { FETCH_PRODUCT_REQUEST,FETCH_PRODUCT_SUCCESS,FETCH_PRODUCT_FAILURE } from "../constants/productConstant";

const initialState={
    products:[],
    error:null
}
const productReducer=(state_initialState,action)=>{
    switch(action.type){
        case FETCH_PRODUCT_REQUEST:
            return{
                ...state,
                error:null
            }
        case FETCH_PRODUCT_SUCCESS:
            return{
                ...state,
                products:action.payload
            }
        case FETCH_PRODUCT_FAILURE:
            return{
                ...state,
                error:action.payload
            }
        default:
            return state
    }
}

export default productReducer
