import { FETCH_PHOTO_REQUEST,FETCH_PHOTO_SUCCESS,FETCH_PHOTO_FAILURE } from "../constants/photoConstant";

const initialState={
    products:[],
    error:null
}
const photoReducer=(state=initialState,action)=>{
    switch(action.type){
        case FETCH_PHOTO_REQUEST:
            return{
                ...state
            }
        case FETCH_PHOTO_SUCCESS:
            return{
                ...state,
                products:action.payload
            }
        case FETCH_PHOTO_FAILURE:
            return{
                ...state,
                error:action.payload
            }
        default:
            return state
    }
}

export default photoReducer