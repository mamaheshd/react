const initialValue={
    student_name:"mahesh dahal"
}
const stusentReducer=(state=initialValue,action)=>{
    switch(action.type){
        case 'CHANGE':
            return{
                ...state,
                student_name:action.payload
            }
        default:
            return state
    }
}

export default stusentReducer