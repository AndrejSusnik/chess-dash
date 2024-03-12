import './Navbar.module.css';

export default function Navbar() {

    return (
        // create a navbar with Home, Categaries, Participants and Results
        // put categories, participants and results on the right of the navbar
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/categories">Categories</a></li>
                <li><a href="/participants">Participants</a></li>
                <li><a href="/results">Results</a></li>
            </ul>
        </nav>
    )

}