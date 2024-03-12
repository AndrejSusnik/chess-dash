import { Match, Show, Switch, createResource } from "solid-js";
import Navbar from "../components/Navbar";
import Category from "../components/Category";
import CategoryModel from "../models/CategoryModel";

export default function Categories() {
  const fetchCategories = async () => {
    const response = await fetch("http://127.0.0.1:5000/categories");

    return response.json();
  };

  const [categories, { mutate, refetch }] = createResource(fetchCategories);

  const addCategory = async () => {};

  return (
    <div>
      <Navbar />
      <div class="flex flex-row">
        <div class="basis-1/2">
          <Show when={categories.loading}>Loading...</Show>
          <Switch>
            <Match when={categories.error}>
              Error: {categories.error.message}
            </Match>
            <Match when={categories()}>
              {categories().map((category: CategoryModel) => (
                <Category {...category} />
              ))}
            </Match>
          </Switch>

          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded"
            onClick={refetch}
          >
            Refresh
          </button>
        </div>
        <div class="basis-1/2">
          <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" use:formSubmit={addCategory}>
            <div class="mb-4">
              <label
                class="block text-gray-700 text-sm font-bold mb-2"
                for="name"
              >
                Name
              </label>
              <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="name"
                type="text"
                placeholder="Name"
              />
            </div>
            <div class="mb-6">
              <label
                class="block text-gray-700 text-sm font-bold mb-2"
                for="description"
              >
                Description
              </label>
              <textarea
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="description"
                placeholder="Description"
              ></textarea>
              <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
                Add
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
