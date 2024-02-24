#include "itemselection.hpp"

#include <MyGUI_Button.h>
#include <MyGUI_TextBox.h>

#include "inventoryitemmodel.hpp"
#include "itemview.hpp"
#include "sortfilteritemmodel.hpp"

namespace MWGui
{

    ItemSelectionDialog::ItemSelectionDialog(const std::string& label)
        : WindowModal("openmw_itemselection_dialog.layout")
        , mSortModel(nullptr)
    {
        getWidget(mItemView, "ItemView");
        mItemView->eventItemClicked += MyGUI::newDelegate(this, &ItemSelectionDialog::onSelectedItem);

        MyGUI::TextBox* l;
        getWidget(l, "Label");
        l->setCaptionWithReplacing(label);

        MyGUI::Button* cancelButton;
        getWidget(cancelButton, "CancelButton");
        cancelButton->eventMouseButtonClick += MyGUI::newDelegate(this, &ItemSelectionDialog::onCancelButtonClicked);

        center();
    }

    bool ItemSelectionDialog::exit()
    {
        eventDialogCanceled();
        return true;
    }

    void ItemSelectionDialog::openContainer(const MWWorld::Ptr& container)
    {
        auto sortModel = std::make_unique<SortFilterItemModel>(std::make_unique<InventoryItemModel>(container));
        mSortModel = sortModel.get();
        mItemView->setModel(std::move(sortModel));
        mItemView->resetScrollBars();
    }

    void ItemSelectionDialog::setCategory(int category)
    {
        mSortModel->setCategory(category);
        mItemView->update();
    }

    void ItemSelectionDialog::setFilter(int filter)
    {
        mSortModel->setFilter(filter);
        mItemView->update();
    }

    void ItemSelectionDialog::onSelectedItem(int index)
    {
        ItemStack item = mSortModel->getItem(index);
        eventItemSelected(item.mBase);
    }

    void ItemSelectionDialog::onCancelButtonClicked(MyGUI::Widget* sender)
    {
        exit();
    }

}
