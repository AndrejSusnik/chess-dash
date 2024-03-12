import CategoryModel from '../models/CategoryModel'; 

export default function Category(props: CategoryModel) {

    return (
        <div>
            <h1>{props.name}</h1>
            <p>{props.description}</p>
        </div>
    )
}