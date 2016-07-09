import React from 'react';
import AutoComplete from 'material-ui/AutoComplete';

export default class Member extends React.Component {
    render () {
        return (
            <AutoComplete
                dataSource={this.props.members}
                onUpdateInput={this.props.handleUpdate.bind(this)}
                openOnFocus={true}
                filter={AutoComplete.noFilter}
                onNewRequest={this.props.signIn.bind(this)}
                errorText={this.props.error}
                hintText="Search members"
                searchText={this.props.searchText}
                fullWidth={true}
            />
        );
    }
}
